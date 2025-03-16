from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.models.order import Order
from app.services.email_service import send_order_confirmation

router = APIRouter()

@router.post("/order-confirmation")
async def create_order_confirmation(order: Order, background_tasks: BackgroundTasks):
    # Process the order
    try:
        # Send email in the background to avoid blocking
        background_tasks.add_task(send_order_confirmation, order)
        return {"status": "success", "message": "Order confirmation email sent"}
    except Exception as e:
        # Log the error
        raise HTTPException(status_code=500, detail=f"Failed to send confirmation: {str(e)}")