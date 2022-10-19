from typing import List

from app import db
from models import User


class UserService:
    def get(
        self,
        *_,
        **kwargs,
    ) -> User:
        return User.query.filter_by(**kwargs).first()

    def list(
        self,
        *_,
        order_by=None,
    ) -> List[User]:
        if not order_by:
            order_by = User.id
        return User.query.order_by(order_by)

    def create(
        self,
        *_,
        **kwargs,
    ) -> User:
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return user

    def update(
        self,
        *_,
        **kwargs,
    ) -> User:
        nickname = kwargs.pop("nickname", None)
        user = UserService().get(nickname=nickname)
        if user:
            user.name = kwargs.pop("name", None)
            user.password = kwargs.pop("password", None)
            db.session.add(user)
            db.session.commit()
        return user