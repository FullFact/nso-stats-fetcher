from datetime import datetime
import logging
import fetch_uk, fetch_ie, fetch_ar, fetch_za, fetch_jp, fetch_mx, fetch_ng

logger = logging.getLogger(__name__)


def add_last_updated():
    # just to keep all server times aligned, stick with UTC time everywhere
    utc_now = datetime.utcnow()
    dt_string = utc_now.strftime("%Y-%m-%d %H:%M:%S")

    out_str = "Last updated: " + dt_string + "\n"
    with open("status.txt", "w") as the_file:
        the_file.write(out_str)


def update_all():
    logger.info("Getting UK data...")
    fetch_uk.fetch_uk_inflation_cpi()
    fetch_uk.fetch_uk_inflation_cpih()
    fetch_uk.fetch_uk_inflation_rpi()

    logger.info("getting Ireland data...")
    fetch_ie.fetch_ie_inflation_cpi()

    logger.info("getting Argentina data...")
    fetch_ar.fetch_ar_inflation_cpi()

    logger.info("getting South Africa data...")
    fetch_za.fetch_za_inflation_cpi()
    fetch_za.fetch_za_inflation_ppi()

    # fetch_ng.fetch_ng_inflation_cpi()
    # fetch_mx.fetch_mx_inflation_cpi()
    # fetch_jp.fetch_jp_inflation_cpi()

    add_last_updated()

    logger.info("Finished update")


if __name__ == "__main__":
    update_all()
