"""Decorator that validates the specified range"""
def validate_range(min_val, max_val):
    """
        Decorator that validates if the argument falls within the specified range.

        Parameters:
        min_val (int): The minimum value of the range.
        max_val (int): The maximum value of the range.

        Returns:
        function: A decorator function
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args)>0 and min_val<= args[0] <= max_val:
                return func(*args, **kwargs)
            # else:
            raise ValueError(f"Argument must be in range of [{min_val}, {max_val}]!")
        return wrapper
    return decorator
