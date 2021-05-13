import numpy as np

def checkValidity() -> bool:
    """
    Checks whether the inputted matrix is square and non-singular. Returns
    True if this is the case, false otherwise.
    """
    if numRows != numCols:
        print("inputted matrix is not square :(")
        return False
    
    if np.linalg.det(inputMatrix) == 0:
        print("inputted matrix is singular :(")
        return False
    
    return True 

if __name__ == "__main__":
    numRows = input("How many rows does your matrix have? : ")
    numCols = input("How many columns does your matrix have? : ")
    inputMatrix = np.empty((2, 2))

    if checkValidity():
        print("inputted matrix is square and non-singular!")