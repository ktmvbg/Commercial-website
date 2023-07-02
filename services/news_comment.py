from dtos import news as news_dto
from models import News, NewsComment, User
from sqlalchemy.orm import Session, joinedload

def create_comment(session: Session, user_id: int, dto: news_dto.CreateNewsCommentInput):
    comment = NewsComment(content=dto.content, user_id=user_id, news_id=dto.news_id)
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return (True, comment)

def update_comment(session: Session, comment_id: int, user_id: int, dto: news_dto.UpdateNewsCommentInput):
    comment = session.query(NewsComment).filter(NewsComment.id==comment_id).first()
    if not comment:
        return (False, 'Comment does not exist')
    if comment.user_id != user_id:
        return (False, 'You are not authorized to update this comment')
    if dto.content:
        comment.content = dto.content
    session.commit()
    session.refresh(comment)
    return (True, comment)

def delete_comment(session: Session, comment_id: int, user_id: int):
    comment = session.query(NewsComment).filter(NewsComment.id==comment_id).first()
    if not comment:
        return (False, 'Comment does not exist')
    user = session.query(User).filter(User.id==user_id).first()
    if comment.user_id != user_id and user.account_type != 2:
        return (False, 'You are not authorized to delete this comment')
    session.delete(comment)
    session.commit()
    return (True, 'Comment deleted')

def get_comments(session: Session, news_id: int, dto: news_dto.GetNewsCommentDto):
    comments = session.query(NewsComment).filter(NewsComment.news_id==news_id).options(joinedload(NewsComment.user))
    if dto.search:
        comments = comments.filter(NewsComment.content.ilike(f'%{dto.search}%'))
    
    comments = comments.order_by(NewsComment.created_at.desc())
    comments = comments.offset((dto.page-1)*dto.page_size).limit(dto.page_size).all()
    
    comments_output = [news_dto.CommentOutput.from_orm(c) for c in comments]
    return (True, comments_output)

def get_comment_by_id(session: Session, comment_id: int):
    comment = session.query(NewsComment).filter(NewsComment.id==comment_id).options(joinedload(NewsComment.user)).first()
    
    if not comment:
        return (False, 'Comment does not exist')
    
    return (True, news_dto.CommentOutput.from_orm(comment))

    
    
    