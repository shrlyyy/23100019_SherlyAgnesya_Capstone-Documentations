import arrow

brewing_time = arrow.utcnow()
brewing_time = brewing_time.to("Europe/Rome")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])
current_chai = chaiProfile(flavor = "Masala", aroma = "Spicy")

print(f"Time in Rome: {brewing_time.format('YYYY-MM-DD HH:mm:ss ZZ')}")
print(f"Chai detail: {current_chai.flavor} with {current_chai.aroma} aroma")