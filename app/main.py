from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from app.fibonacci import calculate_fibonacci

app = FastAPI()

class FibonacciResponse(BaseModel):
    result: int

@app.get("/fib", response_model=FibonacciResponse)
async def get_fibonacci(n: int = Query(..., gt=0)) -> FibonacciResponse:
    """
    n番目のフィボナッチ数を取得

    Parameters
    ----------
    n : int
        計算したいフィボナッチ数の番号

    Returns
    ----------
    FibonacciResponse
        n番目のフィボナッチ数を含むレスポンス
    """
    try:
        result = calculate_fibonacci(n)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return FibonacciResponse(result=result)
