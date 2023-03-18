import configparser

# good easy way to read from config files - configparser [.ini format]
# .ini format:
# [section]
# key = value

cfg = configparser.ConfigParser()
cfg.read("settings.cfg")

print(cfg)
print(cfg["French"])
print(cfg["French"]["greeting"])
print(cfg["files"]["home"])

