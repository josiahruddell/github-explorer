
class FormatUtil(object):
    @staticmethod
    def try_format_str(s, **kwagrs):
        try:
            return s.format(**kwagrs)
        except:
            pass

        return s
