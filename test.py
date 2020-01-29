from py_jwt_validator import PyJwtValidator, PyJwtException

jwt = 'eyJraWQiOiIzZ3p2akJhTU9oaC01enRiRFRrb0tPd1BFTXVCY24wOHhUSkpaQ1lVRGQ4IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwMHVrcWlkMHF1WWJ1WDg2ajBoNyIsIm5hbWUiOiJBZHJpYW4gTGF6xINyIiwiZW1haWwiOiJsenIuYWRyaWFuOTVAZ21haWwuY29tIiwidmVyIjoxLCJpc3MiOiJodHRwczovL2Fkcmlhbi5va3RhcHJldmlldy5jb20iLCJhdWQiOiIwb2FsdGFxNzYyTDBtOEtBUzBoNyIsImlhdCI6MTU4MDI4MTE2MiwiZXhwIjoxNTgwMjg0NzYyLCJqdGkiOiJJRC5oM3VMelFweGd1dkFWcXNwOXo4YXpiTUxKbmpxQzFYX1VfN0JTQ3dCN2hBIiwiYW1yIjpbInB3ZCJdLCJpZHAiOiIwMG9pYW41eDBkb2FFeEpXMDBoNyIsInByZWZlcnJlZF91c2VybmFtZSI6ImFkcmlhbi5sYXphckBhZHJpYW4tbGF6YXIuY29tIiwiYXV0aF90aW1lIjoxNTgwMjgxMTYyLCJhdF9oYXNoIjoiQTZNZkRZaDB6bU5haXRsM1R6dGszQSJ9.BTNUYXbHsXds469I45HsE7YddfMXFZGMusNVFRAz0IO7uB3244LBGIgKajCcDGgBRFZH9W10gy3YPMlXQPoGskqFROkr3NS-Ovy6_V7g-DG_zlZhb1QJulqUX6OmuVjypUPiB-sfl3poSXF4L4LEaPEgRo_y_O3CR6VEX6Fu84U_nX2HRso8OJMfXYC4eWf_mYUVshvklcj7TprbqMnNeB4fghi8_bAISw2FcX-A3_2E28PyFQfiRZvwODcIQkZUJITteR427vDSUdoUkb2ma3xrvLvYxX6Mem1b8RgRf3MS41s1fOOS6MO_LmGFD_3Gy4Qy0mH6gl-_-TVc6MBDng'
try:
    print(PyJwtValidator(jwt, auto_verify=False, check_expiry=False).verify(True))
except PyJwtException as e:
    print(f"Exception caught. Error: {e}")