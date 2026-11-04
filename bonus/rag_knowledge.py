"""BONUS (not covered live): RAG. Let an agent search documents too big to fit in a prompt.

Install the extra packages first:  uv sync --extra bonus
Then run:                          uv run --extra bonus python bonus/rag_knowledge.py

The steps: split the text into chunks, turn each into an embedding, store them, and let
the agent search by meaning. Embeddings use your OpenAI key, at a small cost.
"""

from agno.agent import Agent
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma import ChromaDb

from campus_buddy import MODEL, REPO_ROOT
from campus_buddy.display import show_tools

knowledge = Knowledge(
    vector_db=ChromaDb(
        collection="handbook",
        path="tmp/chroma",
        persistent_client=True,
        embedder=OpenAIEmbedder(),
    )
)
knowledge.insert(path=str(REPO_ROOT / "bonus" / "student_handbook.md"), skip_if_exists=True)

agent = Agent(
    model=MODEL,
    knowledge=knowledge,
    search_knowledge=True,
    instructions="Answer from the handbook. If it doesn't say, say so.",
)

for question in ["What attendance do I need to sit an exam?", "Can I keep a pet in the hostel?"]:
    print(f"\n=== {question}")
    run = agent.run(question)
    show_tools(run)
    print(f"\n{run.content}")
