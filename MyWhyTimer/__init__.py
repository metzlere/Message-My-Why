import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="""To cultivate enduring growth and improvement, 
        so that those I love and those in my orbit are emboldened to be their best. /n
        Live in the Present:/n
            Family time is family time. Practice digital minimalism./n
        Do Your Damn Job:/n
            There are too many soft people in the world. Don't be one of them./n
        Invest in Yourself:/n
            Never stop learning. Reading and doing./n
        'Stand Up Straight With Your Shoulders Back':/n
            Be quiet and be confident. You've been through worse.""",
        from_='+18776068924', 
        to='+18142440043' 
    )


    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
