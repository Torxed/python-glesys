from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
	from .syscalls import SysCommandWorker

class RequirementError(BaseException):
	pass

class SysCallError(BaseException):
	def __init__(self, message :str, exit_code :Optional[int] = None, worker :Optional['SysCommandWorker'] = None) -> None:
		super(SysCallError, self).__init__(message)
		self.message = message
		self.exit_code = exit_code
		self.worker = worker