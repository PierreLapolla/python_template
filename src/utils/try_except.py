# python
from utils.logger import log


def try_except(_func=None, *, finally_callable: callable = None) -> callable:
    """
    Decorator to catch exceptions in a function.
    Optionally execute a callable in the finally block.

    :param _func: The function to decorate.
    :param finally_callable: Optional callable to execute in finally.
    :return: The wrapper function.
    """

    def decorator_func(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                message = f"{func.__name__}: {e.__class__.__name__}: {e}"
                log.error(message)
            finally:
                if finally_callable:
                    finally_callable()

        return wrapper

    if _func is None:
        return decorator_func
    else:
        return decorator_func(_func)


if __name__ == "__main__":
    """
    Example usage of the try_except decorator with a finally callable.
    """

    def cleanup():
        print("Cleanup executed.")

    @try_except(finally_callable=cleanup)
    def divide(a, b):
        return a / b

    divide(1, 0)
