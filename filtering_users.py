from sqlalchemy import and_

from models import Session, User


def main():
    session = Session()
    query = session.query(User).filter(User.salary.between(5000, 6000)
        # and_(
        #     User.salary > 5000,         #to samo co between
        #     User.salary < 6000
        # )
    ).order_by(User.salary.desc())
    # print(query)
    for user in query.limit(5):
        print(user.first_name, user.last_name, user.email, user.salary)
    print('------------------')

    # result = session.query(User).filter(
    #     User.first_name.like('A%')
    # ).scalar()
    # print(result)

    # user = session.query(User).get(42)
    # print(user)

    query = session.query(User.id, User.email, User.creation_date)
    for row in query:
        print(row.id, row.email, row.creation_date)




if __name__ == '__main__':
    main()