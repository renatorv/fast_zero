from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='renatorv', email='renatorv@gmail.com', password='159753'
    )
    session.add(user)
    session.commit()
    # session.refresh(user)
    result = session.scalar(
        select(User).where(User.email == 'renatorv@gmail.com')
    )

    # assert user.id == 1
    assert result.username == 'renatorv'
