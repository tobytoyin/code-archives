def register(params)
	@prefix = params["prefix"]
end

def filter(event)
    # mutate our event by adding a new [prefixMessage] Field
    new_message = "#{@prefix}#{event.get('[message]')}"
    event.set("[prefixMessage]", new_message)
    return [event]
end