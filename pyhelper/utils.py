import bge

clamp = lambda v,mi,ma : max(mi, min(v, ma))

KEY_LIST = {
	"mouse" : [k for k in dir(bge.events) if not k.startswith("__") and "MOUSE" in k],
	"keyboard" : [k for k in dir(bge.events) if not k.startswith("__") and not any(l in k for l in ["MOUSE", "EventToCharacter", "EventToString"])],
}
