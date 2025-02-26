import time
import os.path
import random

from botclient.botcache import BotCache

def generate_stuff(d, format, nlines):
	"""Generates a file of timestamped random stuff for testing"""
	ts = str(time.time())
	file = os.path.join(d, ts + '.log')
	stuff = [ "# here are", "# some comments" ]
	for i in range(nlines):
		babble = ''.join([ random.choice('AGTC') for k in range(10) ])
		stuff.append(ts + '.' + babble + '.' + str(i))
	with open(file, 'w') as fh:
		if format == 'txt':
			fh.writelines([ l + '\n' for l in stuff])
		else:
			fh.write(json.dumps(stuff, indent=4))
	return stuff

def test_cache(tmp_path):
    cache = BotCache({ "dir": str(tmp_path), "cache_max": 8, format: "txt"})
    fresh = generate_stuff(str(tmp_path), cache.format, 100)
    cache.put(fresh)
    for line in [ l for l in fresh if len(l) > 0 and l[0] != '#']:
        cache_line = cache.get()
        assert(cache_line == cache)

        


