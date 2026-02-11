#3. Terdapat dua set yang berisi daftar keahlian (skill) dari dua tim pengembang:
#tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
#tim_backend = {"Python", "JavaScript", "SQL",
#"NodeJS"}
#1. Tentukan keahlian yang dimiliki oleh kedua tim (irisan).
#2. Tentukan keahlian yang hanya dimiliki oleh tim_backend.
#3. Gabungkan kedua set tersebut untuk melihat daftar total keahlian unik yang
#tersedia di perusahaan.

tim_frontend={"HTML", "CSS","Javascript","React"}
tim_backend={"Python","Javascript","SQL"}

keahlian_keduatim = tim_frontend & tim_backend
keahlian_keduatim1 = tim_frontend.difference(tim_backend)
tim_frontend.update(tim_backend)
print(keahlian_keduatim)
print(keahlian_keduatim1)
print(tim_frontend)