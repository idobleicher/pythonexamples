# def main(app, freq=2.0):
#     state = app.events.State()
#     with myapp.connection() as connection:
#         recv = app.events.Receiver(connection, handlers={'*': state.event})
#         with DumpCam(state, freq=freq):
#             recv.capture(limit=None, timeout=None)
#
# if __name__ == '__main__':
#     main(myapp)