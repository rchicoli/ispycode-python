
import platform

system = platform.system()
release = platform.release()
version = platform.version()

print(system)
print(release)
print(version)

print(platform.system_alias(system, release, version))


