import mailtrap as mt
from jinja2 import Environment, FileSystemLoader

# noinspection PyPackages
from ..config import settings
# noinspection PyPackages
from ..models.order import Order

# Setup Jinja2 template environment
env = Environment(loader=FileSystemLoader("app/templates"))


def send_order_confirmation(order: Order):
    # Load template
    template = env.get_template("order_confirmation.html")

    # Render HTML with order details
    html_content = template.render(
        order=order,
        company_name=settings.COMPANY_NAME,
        support_email=settings.SUPPORT_EMAIL,
    )

    # Create text version
    text_content = f"""
    Thank you for your order #{order.order_id}!

    Order Total: ${order.total:.2f}

    Visit our website for more details.
    """

    # Setup mail content using the correct Mailtrap API pattern
    mail = mt.Mail(
        sender=mt.Address(email=settings.EMAIL_SENDER, name=settings.COMPANY_NAME),
        to=[mt.Address(email=order.customer.email, name=order.customer.name)],
        subject=f"Your Order Confirmation #{order.order_id}",
        text=text_content,
        html=html_content,
        category="Order Confirmation"
    )

    # Send email
    client = mt.MailtrapClient(token=settings.MAILTRAP_API_TOKEN)
    return client.send(mail)