from models import Session, User


def main():
    session = Session()
    query = session.query(User).filter(User.salary > 9000)
    # print(query)
    for user in query.limit(5):
        print(user.first_name, user.last_name, user.email, user.salary)



if __name__ == '__main__':
    main()