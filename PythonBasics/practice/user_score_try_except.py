class User:

    def __init__(self, name, engagement_metrics):
        self.name = name
        self.engagement_metrics = engagement_metrics
        self.score = 0  # initialize score with 0

    def __repr__(self):
        return f"User: {self.name}"


def send_email_notification_on_success(user):
    try:
        print(f"Performing score calculations for {user.name}")
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError as exc:
        print("Invalid entry!")
        raise RuntimeError("Something bad happened") from exc # observe that finally is still executed before raising RuntimeError
    else:
        if(user.score >= 500):
            send_email_to_user(user)
        else:
            print(f"Insufficient score of {user.score}")
    finally:
        print("Inside finally")


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2 # random Score calculation logic


def send_email_to_user(user):
    print(f"Great score of {user.score}!   Email notification sent to: {user}")


# Try Exception case
#user = User("Shirish",{'click':3,'hits':2})
#send_email_notification_on_success(user)

print("-" * 20)

user = User("Nita",{'clicks':30,'hits':200})
send_email_notification_on_success(user)