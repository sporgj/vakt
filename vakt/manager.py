from abc import ABCMeta, abstractmethod


class PolicyManager(metaclass=ABCMeta):
    """Interface for managers that persist policies.
    Every manager should implement all the specified methods, but how, it's up to it to decide:
    it can be in-memory storage, SQL database, NoSQL solution, etc."""

    @abstractmethod
    def create(self, policy):
        """Create a policy"""
        pass

    @abstractmethod
    def get(self, id):
        """Retrieve specific policy"""
        pass

    @abstractmethod
    def get_all(self, limit, offset):
        """Retrieve all the policies within a window"""
        pass

    @abstractmethod
    def find_by_inquiry(self, inquiry):
        """
        Get potential policies for a given inquiry.
        Managers are free to decide what policies to return based on the performance and implementation considerations.
        In the worst case - all policies. In the best - policies matched on actions, subjects, resources.
        Mediocre case - match on subject.
        """
        pass

    @abstractmethod
    def update(self, policy):
        """Update a policy"""
        pass

    @abstractmethod
    def delete(self, id):
        """Delete a policy"""
        pass


class Migration(metaclass=ABCMeta):
    """Class for Manager data migration tasks.
    Useful mainly for relational databases."""

    @abstractmethod
    def get_manager(self):
        """Gets a Manager to use for migration"""
        pass

    @abstractmethod
    def create(self, policy):
        """Create a Policy inside DB"""
        pass

    @abstractmethod
    def migrate(self):
        """Migrate a Policy schema"""
        pass
