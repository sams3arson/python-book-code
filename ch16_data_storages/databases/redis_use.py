import redis

conn = redis.Redis("localhost")

print(conn.keys("*"))

# set() returns True if operation went successfully
conn.set("secret", "ni!")
conn.set("carats", 24)
conn.set("fever", "101.5")

print(conn.get("secret"))
print(conn.get("carats"))
print(conn.get("fever"))

# setnx() only sets value if key doesn't exist yet
conn.setnx("secret", "icky-icky-icky-ptang-zoop-boing!")

conn.mget(["fever", "carats"])

conn.delete("fever")


print("##### lists")
# redis lists
# list is being created when you push first data
conn.lpush("zoo", "bear")
print(conn.lrange("zoo", 0, -1))
conn.lpush("zoo", "alligator", "duck")
print(conn.lrange("zoo", 0, -1))

conn.linsert("zoo", "before", "bear", "beaver")
print(conn.lrange("zoo", 0, -1))
conn.linsert("zoo", "after", "bear", "cassowary")
print(conn.lrange("zoo", 0, -1))

conn.lset("zoo", 2, "marmoset")
print(conn.lrange("zoo", 0, -1))
conn.rpush("zoo", "yak")

print(conn.lindex("zoo", 3))

print(conn.lrange("zoo", 0, 2))

print(conn.lrange("zoo", 0, -1))
print(conn.ltrim("zoo", 1, 4))


print("##### hashes")
# redis hashes
conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})
conn.hset("song", "mi", "a note to follow re")
print(conn.hget("song", "mi"))
print(conn.hkeys("song"))
print(conn.hvals("song"))
print(conn.hlen("song"))
conn.hsetnx("song", "fa", "a note that rhymes with la")

