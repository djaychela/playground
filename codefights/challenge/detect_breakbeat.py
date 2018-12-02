def detectBreakbeat(pattern):
    pattern = pattern.split()
    if len(pattern) <= 4:
        return False
    length = len(pattern)
    k1 = int(length / 8 * 3)
    k2 = int(length / 8 * 5)
    if pattern[0] == '~':
        return False
    if pattern[k1] != pattern[0] and pattern[k2] != pattern[0]:
        return False
    s1 = int(length / 8 * 2)
    s2 = int(length / 8 * 6)
    if pattern[s1] == '~':
        return False
    if pattern[s1] != pattern[s2] or pattern[0] == pattern[s1]:
        return False
    return True

# pattern= "bd sn bd sn"
# pattern = "clubkick:2 ~ hc ~ ~ clubkick:2 hc ~"
#
# print(detectBreakbeat(pattern))
#
# pattern = "subkick hh ~ hh clap hh subkick hh ~ hh subkick hh clap ~ hh hh"
#
# print(detectBreakbeat(pattern))

pattern = "bd bd bd ~ ~ sn bd bd cp ~ bd ~ ~ sn cp cp"
print(detectBreakbeat(pattern))