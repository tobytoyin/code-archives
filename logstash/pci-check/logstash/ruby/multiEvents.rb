def register(params)
  @delim = params["delim"]
end

def filter(event)
    new_events = []

    # populate into multi events if we can split by ','
    messages_str = event.get('[message]')
    messages = messages_str.split(@delim)

    # use a for-loop on our array of messages, then
    # clone multiple events and mutate them as multiple events
    messages.each do |message|
        tmpEvent = event.clone
        tmpEvent.set('[message]', message)
        new_events << tmpEvent
    end

    return new_events
end


def pci_redaction()
  return "hello world"
end