from userManagement.util.ResponseUtil import ResponseEntity
from userManagement.repository.UserRepository import UserRepository

class UserController:

    @staticmethod
    def registerUser(user=None):
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getAllUser():
        responseBody = UserRepository.getUsersAll()
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getUserByUsername(username=None):
        responseBody = UserRepository.selectUserByUsername(username)
        return ResponseEntity(body=responseBody)

    @staticmethod
    def updateUser(user=None):
        responseBody = UserRepository.updateUser(user)
        return ResponseEntity(body=responseBody)

    @staticmethod
    def deleteUser(user=None):
        responseBody = UserRepository.deleteUser(user)
        return ResponseEntity(body=responseBody)