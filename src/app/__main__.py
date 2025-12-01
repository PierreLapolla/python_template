from pedros.logger import get_logger


def main() -> None:
    logger = get_logger(__name__)
    logger.info("Hello from python-template!")


if __name__ == "__main__":
    main()
