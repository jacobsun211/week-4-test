יעקב שמש
נגב
325606481




































from sqlmodel import SQLModel, Field, create_engine, Session, select
from datetime import date, datetime
from sqlalchemy import Text, Date, Column, delete
from typing import Optional
import mysql.connector

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d")

cnx_url = f"mysql://root@localhost:3306/agents"
engine = create_engine(cnx_url)
SQLModel.metadata.create_all(engine)

cnx = mysql.connector.connect(
    user="root",
    password='',
    host='127.0.0.1',
    port=3306,
    database='agents',
)

# Creating tables
class agents(SQLModel, table=True):
    agentId: int = Field(default=None, primary_key=True)
    agentName: str = Field(unique=True)
    clearance: int


class terrorists(SQLModel, table=True):
    terroristId: int = Field(default=None, primary_key=True)
    terroristName: str = Field(unique=True)


class reports(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    agentId: int = Field(foreign_key="agents.agentId")
    content: str = Field(sa_column=Column(Text))
    reportTime: date = Field(sa_column=Column(Date))


class Reports_Terrorists(SQLModel, table=True):
    #   id: Optional[int] = Field(default=None, primary_key=True)  # Add primary key
    reportsId: int = Field(foreign_key="reports.id", primary_key=True)
    terroristId: int = Field(foreign_key="terrorists.terroristId", primary_key=True)


# Insert agent
login_agent = agents(agentName='wolf', clearance=2)


def add_agent(login_agent):
    with Session(engine) as session:
        session.add(login_agent)
        session.commit()
        session.refresh(login_agent)
        print(f"Agent created: {login_agent}")


# Insert terrorists
terrorist1 = terrorists(terroristName='abu mazen')
terrorist2 = terrorists(terroristName='unknown')


# def add_terrorists(terrorist):
#     with Session(engine) as session:
#         session.add(terrorist)
#         session.commit()
#         session.refresh(terrorist)


def add_report(login_agent):
    # Create report
    add_report = reports(
        agentId=login_agent.agentId,
        content='im going to bomb this place in 3 days',
        reportTime=timestamp
    )
    with Session(engine) as session:
        session.add(add_report)
        session.commit()
        session.refresh(add_report)
        print(f"Report created: {add_report}")
        return add_report


def add_Reports_Terrorists(report, terrorist1, terrorist2=None, terrorist3=None, terrorist4=None):
    # Link multiple terrorists to this report
    with Session(engine) as session:
        link1 = Reports_Terrorists(reportsId=report.id, terroristId=terrorist1.terroristId)
        session.add(link1)
        if terrorist2:
            link2 = Reports_Terrorists(reportsId=report.id, terroristId=terrorist2.terroristId)
            session.add(link2)
        if terrorist3:
            link3 = Reports_Terrorists(reportsId=report.id, terroristId=terrorist2.terroristId)
            session.add(link3)
        if terrorist4:
            link4 = Reports_Terrorists(reportsId=report.id, terroristId=terrorist2.terroristId)
            session.add(link4)
        session.commit()
        print("Terrorists linked to report")

# add_agent(login_agent)
# add_terrorists(terrorist1)
# add_terrorists(terrorist2)
# report = add_report(login_agent)
# add_Reports_Terrorists(report,terrorist1,terrorist2)
# print('done')


# Query: Get all terrorists for a specific report
# with Session(engine) as session:
#     statement = select(terrorists).join(Reports_Terrorists).where(Reports_Terrorists.reportsId == 4)
#     result = session.exec(statement).all()
#     print(f"\nTerrorists in report 1: {result}")






def delete_report(agent):
 with Session(engine) as session:
     statement = delete(reports).where(reports.agentId == agent.agentId)
     session.exec(statement)
     session.commit()
