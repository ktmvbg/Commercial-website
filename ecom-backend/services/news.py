from dtos import news as news_dto
from models import News, NewsComment
from sqlalchemy.orm import Session, joinedload

def create_news(session: Session, user_id: int, dto: news_dto.CreateNewsInput):
    news = News(title=dto.title, content=dto.content, image=dto.image, user_id=user_id)
    session.add(news)
    session.commit()
    session.refresh(news)
    return (True, news)

def update_news(session: Session, news_id: int, user_id: int, dto: news_dto.UpdateNewsInput):
    news = session.query(News).filter(News.id==news_id).first()
    if not news:
        return (False, 'News does not exist')
    if news.user_id != user_id:
        return (False, 'You are not authorized to update this news')
    if dto.title:
        news.title = dto.title
    if dto.content:
        news.content = dto.content
    if dto.image:
        news.image = dto.image
    session.commit()
    session.refresh(news)
    return (True, news)

def delete_news(session: Session, news_id: int):
    news = session.query(News).filter(News.id==news_id).first()
    if not news:
        return (False, 'News does not exist')
    session.delete(news)
    session.commit()
    return (True, 'News deleted')

def get_news(session: Session, dto: news_dto.GetNewsDto):
    news = session.query(News).options(joinedload(News.user))
    if dto.search:
        news = news.filter((News.title.ilike(f'%{dto.search}%')) | (News.content.ilike(f'%{dto.search}%')))       
        
    if dto.from_date:
        news = news.filter(News.created_at >= dto.from_date)
    
    if dto.to_date:
        news = news.filter(News.created_at <= dto.to_date)
        
    if dto.user_id:
        news = news.filter(News.user_id == dto.user_id)   
        
    news = news.order_by(News.created_at.desc())
    news = news.offset((dto.page-1)*dto.page_size).limit(dto.page_size).all()
    
    news_output = [news_dto.NewsOutput.from_orm(n) for n in news]
    return (True, news_output)

def get_news_by_id(session: Session, news_id: int):
    news = session.query(News).filter(News.id==news_id).options(joinedload(News.user)).first()
    
    if not news:
        return (False, 'News does not exist')
    return (True, news_dto.NewsOutput.from_orm(news))    
    