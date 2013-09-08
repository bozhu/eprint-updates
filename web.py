"""
    Copyright (C) 2012 Bo Zhu http://about.bozhu.me

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
"""

import webapp2
import cron_task
import logging


class CronHandler(webapp2.RequestHandler):
    def get(self):
        try:
            cron_task.task()
        except Exception as detail:
            from report import report_error
            import traceback
            report_error(
                str(detail).splitlines()[0],  # title shouldn't be too long
                traceback.format_exc()
            )


class TestHandler(webapp2.RequestHandler):
    def get(self):
        cron_task.task()


# is here a proper position for setting log level?
logging.getLogger().setLevel(logging.DEBUG)

app = webapp2.WSGIApplication([
    ('/cron', CronHandler),
    ('/test', TestHandler),
], debug=True)
