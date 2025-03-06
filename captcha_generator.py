from captcha.image import ImageCaptcha
import random
import string
def generate_captcha():
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    image = ImageCaptcha(width=200, height=80)

    captcha_image = image.generate_image(captcha_text)


    image_path = f"{captcha_text}.png"
    captcha_image.save(image_path)

    print(f"CAPTCHA generated: {captcha_text}, saved as {image_path}")

if __name__ == "__main__":
    generate_captcha()