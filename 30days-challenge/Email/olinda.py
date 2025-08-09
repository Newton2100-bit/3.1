# import logging
# import logging.handlers
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
#
# # Configure email logging
# def setup_email_logging():
#     logger = logging.getLogger("email_logger")
#     logger.setLevel(logging.ERROR)  # Only send ERROR and CRITICAL messages
#
#     # SMTP Handler configuration
#     smtp_handler = logging.handlers.SMTPHandler(
#         mailhost=("smtp.gmail.com", 587),  # Gmail SMTP
#         fromaddr="adabyron005@gmail.com",
#         toaddrs=["olindamuruginyaga@gmail.com"],
#         subject="Application Error Log",
#         credentials=("adabyron005@gmail.com", "newtonirungu"),
#         secure=(),  # Use TLS
#     )
#
#     # Set formatter
#     formatter = logging.Formatter(
#         "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#     )
#     smtp_handler.setFormatter(formatter)
#
#     logger.addHandler(smtp_handler)
#     return logger
#
#
# # Usage example
# if __name__ == "__main__":
#     logger = setup_email_logging()
#
#     # These will be sent via email
#     logger.error("This is an error message")
#     logger.critical("This is a critical error")
#
#     # This won't be sent (below ERROR level)
#     logger.warning("This warning won't be emailed")

import logging
import logging.handlers
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os  # For environment variables


def setup_email_logging():
    logger = logging.getLogger("email_logger")
    logger.setLevel(logging.DEBUG)

    # Get credentials from environment variables (more secure)
    email = os.getenv("EMAIL_USER", "adabyron005@gmail.com")
    password = 'cusy liso meey gwdy'  # Use App Password

    if not password:
        print("Warning: No email password found in environment variables")
        return logger

    smtp_handler = logging.handlers.SMTPHandler(
        mailhost=("smtp.gmail.com", 587),
        fromaddr=email,
        toaddrs= ['mwauranewton99@gmail.com'], #["olindamuruginyaga@gmail.com"],
        subject="Application Error Log",
        credentials=(email, password),
        secure=(),
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    smtp_handler.setFormatter(formatter)
    logger.addHandler(smtp_handler)
    return logger


if __name__ == "__main__":  # Fixed the syntax error
    logger = setup_email_logging()
    logger.error("This is an error message")
    logger.critical("This is a critical error")
    logger.warning("This warning won't be emailed")
