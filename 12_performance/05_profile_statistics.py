import pstats
import pystone
import cProfile


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.runcall(pystone.main)
    profiler.dump_stats('pystone.profile')

    stats = pstats.Stats('pystone.profile')
    stats.strip_dirs()
    stats.sort_stats('calls', 'cumtime')
    stats.print_stats(10)
