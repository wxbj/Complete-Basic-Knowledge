"""
cmath
Help on built-in module cmath:

NAME
    cmath

DESCRIPTION
    This module provides access to mathematical functions for complex
    numbers.

FUNCTIONS
    acos(z, /)
        Return the arc cosine of z.

    acosh(z, /)
        Return the inverse hyperbolic cosine of z.

    asin(z, /)
        Return the arc sine of z.

    asinh(z, /)
        Return the inverse hyperbolic sine of z.

    atan(z, /)
        Return the arc tangent of z.

    atanh(z, /)
        Return the inverse hyperbolic tangent of z.

    cos(z, /)
        Return the cosine of z.

    cosh(z, /)
        Return the hyperbolic cosine of z.

    exp(z, /)
        Return the exponential value e**z.

    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two complex numbers are close in value.

          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values

        Return True if a is close in value to b, and False otherwise.

        For the values to be considered close, the difference between them must be
        smaller than at least one of the tolerances.

        -inf, inf and NaN behave similarly to the IEEE 754 Standard. That is, NaN is
        not close to anything, even itself. inf and -inf are only close to themselves.

    isfinite(z, /)
        Return True if both the real and imaginary parts of z are finite, else False.

    isinf(z, /)
        Checks if the real or imaginary part of z is infinite.

    isnan(z, /)
        Checks if the real or imaginary part of z not a number (NaN).

    log(...)
        log(z[, base]) -> the logarithm of z to the given base.

        If the base not specified, returns the natural logarithm (base e) of z.

    log10(z, /)
        Return the base-10 logarithm of z.

    phase(z, /)
        Return argument, also known as the phase angle, of a complex.

    polar(z, /)
        Convert a complex from rectangular coordinates to polar coordinates.

        r is the distance from 0 and phi the phase angle.

    rect(r, phi, /)
        Convert from polar coordinates to rectangular coordinates.

    sin(z, /)
        Return the sine of z.

    sinh(z, /)
        Return the hyperbolic sine of z.

    sqrt(z, /)
        Return the square root of z.

    tan(z, /)
        Return the tangent of z.

    tanh(z, /)
        Return the hyperbolic tangent of z.

DATA
    e = 2.718281828459045
    inf = inf
    infj = infj
    nan = nan
    nanj = nanj
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)
"""