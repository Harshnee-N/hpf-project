import logging
import requests

logger = logging.getLogger(__name__)


def verify_booking(booking):
    try:
        response = requests.post(
            "https://httpbin.org/post",
            json={
                "booking_id": booking.id,
                "parent_id": booking.parent_id,
                "lsa_id": booking.lsa_id,
            },
            timeout=5
        )

        response.raise_for_status()

        return True

    except requests.RequestException as e:
        logger.error("Booking verification failed: %s", e)
        return False