import hashlib

def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_login):
        
    if email in stored_login:   # Check if email exists in stored logins
          stored_hash = stored_login[email] # get stored hash
          return stored_hash == hash_password(password_to_check) # compare hashes
    return False   # Return False if email not found


def main():
      stored_login ={
            "user@gmail.com": hash_password("securepassword123"),
            "abc@gmail.com": hash_password("mypassword")
      }

      email = input("Enter your email:")
      password = input("Enter your password:")

      if login(email, password, stored_login):
            print("Login Successful!✅")
      else:
        print("Login failed! ❌ Incorrect email or password.")

if __name__ == '__main__':
    main()