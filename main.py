from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "sqlite:///./litbyte_authors.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class AuthorNovel(Base):
    __tablename__ = "author_novels"

    id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String, index=True)
    novel_title = Column(String, index=True)
    plot = Column(String)
    characters = Column(String)
    themes = Column(String)
    analysis = Column(String)


app = FastAPI(
    title="LitByte Backend",
    description="Permanent storage for Indian authors and their novels",
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def insert_sample_data():
    db: Session = SessionLocal()
    try:
        if db.query(AuthorNovel).count() > 0:
            return

        samples = [
            AuthorNovel(author_name="R.K. Narayan", novel_title="Swami and Friends", plot="Childhood story of Swami in Malgudi.", characters="Swami, Mani, Rajam", themes="Childhood, friendship, school life", analysis="Shows the innocence of childhood."),
            AuthorNovel(author_name="R.K. Narayan", novel_title="The Guide", plot="Raju becomes a guide and spiritual figure.", characters="Raju, Rosie, Marco", themes="Transformation, fame, spirituality", analysis="A classic study of change."),
            AuthorNovel(author_name="R.K. Narayan", novel_title="Waiting for the Mahatma", plot="A youth joins the freedom movement.", characters="Sriram, Bharati, Gandhi", themes="Nationalism, youth, love", analysis="Combines romance with politics."),
            AuthorNovel(author_name="Ruskin Bond", novel_title="The Room on the Roof", plot="Rusty runs away to seek freedom.", characters="Rusty, friends, guardian", themes="Identity, freedom, belonging", analysis="A coming-of-age classic."),
            AuthorNovel(author_name="Ruskin Bond", novel_title="A Flight of Pigeons", plot="A family faces the 1857 revolt.", characters="Ruth, family, local people", themes="History, conflict, survival", analysis="Gentle historical fiction."),
            AuthorNovel(author_name="Ruskin Bond", novel_title="The Blue Umbrella", plot="A village girl gets a special umbrella.", characters="Binya, villagers, shopkeeper", themes="Innocence, envy, kindness", analysis="A tender village story."),
            AuthorNovel(author_name="Arundhati Roy", novel_title="The God of Small Things", plot="Twins face a tragic family story.", characters="Estha, Rahel, Ammu, Velutha", themes="Caste, trauma, family", analysis="A landmark non-linear novel."),
            AuthorNovel(author_name="Arundhati Roy", novel_title="The Ministry of Utmost Happiness", plot="Many lives connect across India.", characters="Anjum, Tilo, Musa", themes="Identity, gender, politics", analysis="A layered social novel."),
            AuthorNovel(author_name="Vikram Seth", novel_title="A Suitable Boy", plot="Lata searches for a husband.", characters="Lata, suitors, families", themes="Marriage, family, change", analysis="Epic post-independence novel."),
            AuthorNovel(author_name="Vikram Seth", novel_title="An Equal Music", plot="A violinist revisits love and music.", characters="Michael, Julia, musicians", themes="Music, love, memory", analysis="A lyrical modern novel."),
            AuthorNovel(author_name="Chetan Bhagat", novel_title="Five Point Someone", plot="Three friends struggle in IIT.", characters="Hari, Ryan, Alok", themes="Education pressure, friendship", analysis="Popular youth fiction."),
            AuthorNovel(author_name="Chetan Bhagat", novel_title="2 States", plot="A couple faces family opposition.", characters="Krish, Ananya, families", themes="Love, culture, marriage", analysis="Mass-market romantic fiction."),
            AuthorNovel(author_name="Mulk Raj Anand", novel_title="Untouchable", plot="A day in Bakha's life.", characters="Bakha, Sohini, Lakha", themes="Caste, dignity, injustice", analysis="Powerful social protest novel."),
            AuthorNovel(author_name="Mulk Raj Anand", novel_title="Coolie", plot="Munoo suffers exploitation.", characters="Munoo, workers, employers", themes="Child labor, poverty, class", analysis="Harsh realism about labor."),
            AuthorNovel(author_name="Raja Rao", novel_title="Kanthapura", plot="A village joins the freedom struggle.", characters="Moorthy, Rangamma, villagers", themes="Nationalism, Gandhism, resistance", analysis="Blends politics and oral storytelling."),
            AuthorNovel(author_name="Salman Rushdie", novel_title="Midnight's Children", plot="Saleem's life mirrors India's history.", characters="Saleem, Shiva, Parvati", themes="History, magic realism, nationhood", analysis="A major postcolonial novel."),
            AuthorNovel(author_name="Khushwant Singh", novel_title="Train to Pakistan", plot="Partition disrupts a village.", characters="Jugga, Nooran, Iqbal", themes="Partition, violence, sacrifice", analysis="Moving Partition novel."),
            AuthorNovel(author_name="Rohinton Mistry", novel_title="A Fine Balance", plot="Four lives under political turmoil.", characters="Dina, Ishvar, Om, Maneck", themes="Survival, poverty, politics", analysis="Deeply emotional social novel."),
            AuthorNovel(author_name="Jhumpa Lahiri", novel_title="The Namesake", plot="Gogol struggles with identity.", characters="Gogol, Ashoke, Ashima", themes="Immigration, identity, family", analysis="A key immigrant novel."),
            AuthorNovel(author_name="Jhumpa Lahiri", novel_title="Interpreter of Maladies", plot="Stories of displacement and intimacy.", characters="Various families", themes="Loneliness, communication, migration", analysis="Quiet emotional depth."),
            AuthorNovel(author_name="Kiran Desai", novel_title="The Inheritance of Loss", plot="Lives in Kalimpong and New York.", characters="Sai, Biju, Jemubhai", themes="Colonial legacy, migration, class", analysis="Darkly humorous and global."),
            AuthorNovel(author_name="Anita Desai", novel_title="Fasting, Feasting", plot="Contrasting lives in India and America.", characters="Uma, Arun, parents", themes="Gender roles, culture clash", analysis="Powerful domestic novel."),
            AuthorNovel(author_name="Shashi Deshpande", novel_title="That Long Silence", plot="A woman reflects on her marriage.", characters="Jaya, Mohan", themes="Marriage, voice, selfhood", analysis="Landmark feminist novel."),
            AuthorNovel(author_name="Manju Kapur", novel_title="Difficult Daughters", plot="A daughter learns her mother's past.", characters="Virmati, Ida, Harish", themes="Women, independence, family", analysis="Historical feminist fiction."),
            AuthorNovel(author_name="Aravind Adiga", novel_title="The White Tiger", plot="A driver rises from poverty.", characters="Balram, Ashok, Pinky Madam", themes="Class, corruption, ambition", analysis="Dark social satire."),
            AuthorNovel(author_name="Amish Tripathi", novel_title="The Immortals of Meluha", plot="Mythological retelling of Shiva.", characters="Shiva, Sati, Daksha", themes="Mythology, heroism, destiny", analysis="Popular mythological fiction."),
            AuthorNovel(author_name="Amish Tripathi", novel_title="The Secret of the Nagas", plot="Shiva continues his quest.", characters="Shiva, Sati, Nagas", themes="Mythology, conflict, truth", analysis="Adventure-driven mythic tale."),
            AuthorNovel(author_name="Anita Nair", novel_title="Ladies Coupe", plot="A woman journeys and reflects.", characters="Akhila, passengers", themes="Freedom, self-discovery, patriarchy", analysis="Women-centered journey novel."),
            AuthorNovel(author_name="Shashi Tharoor", novel_title="The Great Indian Novel", plot="Indian history retold satirically.", characters="Mythic and political figures", themes="Satire, politics, history", analysis="Ingenious political parody."),
            AuthorNovel(author_name="Bharati Mukherjee", novel_title="Jasmine", plot="A woman reinvents herself in America.", characters="Jasmine, Prakash, Taylor, Bud", themes="Migration, identity, reinvention", analysis="A classic immigrant novel."),
        ]

        db.add_all(samples)
        db.commit()
    finally:
        db.close()


insert_sample_data()


@app.get("/search")
def search_novels(q: str, db: Session = Depends(get_db)):
    results = db.query(AuthorNovel).filter(
        (AuthorNovel.author_name.ilike(f"%{q}%")) |
        (AuthorNovel.novel_title.ilike(f"%{q}%")) |
        (AuthorNovel.plot.ilike(f"%{q}%")) |
        (AuthorNovel.characters.ilike(f"%{q}%")) |
        (AuthorNovel.themes.ilike(f"%{q}%")) |
        (AuthorNovel.analysis.ilike(f"%{q}%"))
    ).all()

    return [
        {
            "author_name": r.author_name,
            "novel_title": r.novel_title,
            "plot": r.plot,
            "characters": r.characters,
            "themes": r.themes,
            "analysis": r.analysis,
        }
        for r in results
    ]