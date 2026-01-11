# A:
except (TypeError, ValueError, ZeroDivisionError):
    # Some code.

# B:
except TypeError, ValueError, ZeroDivisionError:
    # Some code.

# C:
except: (TypeError, ValueError, ZeroDivisionError)
    # Some code.

# D:
except: TypeError, ValueError, ZeroDivisionError
    # Some code.

# E:
except (TypeError, ValueError, ZeroDivisionError)
    # Some code.

# F:
except TypeError, ValueError, ZeroDivisionError
    # Some code.

