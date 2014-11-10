class Dispatcher:
  def init(self):
    self.observer_events = {}

  def add_observer(self, observer, event):
    if(event==None):
      raise ValueError('Event must be supplied')
    else:
      # init 
      if(event not in self.observer_events):
        self.observer_events[event] = []

      # check for duplicates
      if(observer in self.observer_events[event]):
        return

      # add to list for that particular events
      self.observer_events[event].append(observer)

  def notify_observers(self, event):
    if(event==None):
      raise ValueError('Event must be supplied')
    else:
      # check if exists
      if(self.observer_events[event]==None):
        return

      # notify all observers
      for observer in self.observer_events[event]:
        observer()

  def remove_observer(self, observer, event=None):
    if(event==None):
      # remove observer from all events
      for observer_events in self.observer_events:
        observer_events.remove(observer)
    else:
      observers = self.observer_events[event]
      observers.remove(observer)



