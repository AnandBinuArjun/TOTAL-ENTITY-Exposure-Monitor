from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, JSON
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class ExposureEvent(Base):
    __tablename__ = "exposure_events"
    id = Column(Integer, primary_key=True, index=True)
    identifier_hash = Column(String, index=True)
    breach_source = Column(String)
    detected_at = Column(DateTime, default=datetime.utcnow)
    data_classes = Column(JSON)

class IdentityNode(Base):
    __tablename__ = "identity_nodes"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    type = Column(String)
    risk_score = Column(Float)
    
class ActionPlan(Base):
    __tablename__ = "action_plans"
    id = Column(Integer, primary_key=True)
    identifier = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    actions = Column(JSON)
