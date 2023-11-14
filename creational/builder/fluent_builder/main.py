from email_builder import EmailBuilder

def main():
    email_message = (
        EmailBuilder()
        .add_from("info@test.com")
        .add_to("john@test.com")
        .add_to("jane@test.com")
        .add_cc("jones@test.com")
        .with_subject("The Builder Pattern")
        .with_body("Checkout this awsome builder pattern tutorial")
        .add_attachment("builder_pattern.pdf")
        .build()
    )
    email_message.send()

if __name__ == "__main__":
    main()
        
