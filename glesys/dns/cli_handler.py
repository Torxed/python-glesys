import json

from ..output import log, stylize_output

def dns_entrypoint(args, **kwargs):
	from ..session import session

	if args.all_domains:
		result = json.dumps(session['api'].dns.all_domains(), indent=4)
		if args.color:
			result = result.replace('"usingglesysnameserver": "no",', stylize_output('"usingglesysnameserver": "no",', fg="orange"))
			result = result.replace('"state": "EXPIRING60",', stylize_output('"state": "EXPIRING60",', fg="red"))
		print(result)
	elif args.all_records:
		print(json.dumps(session['api'].dns.all_records(args.domain), indent=4))

	elif args.find:
		print(list(session['api'].dns.find(domain=args.domain, record=args.record, type=args.type, data=args.data)))

	elif args.add:
		session['api'].dns.add_record(args.domain, {
			'host': args.record,
			'data': args.data,
			'type': args.type,
			'ttl': args.ttl
		})

	elif args.delete:
		session['api'].dns.delete_record(args.domain, {
			'host': args.record,
			'data': args.data,
			'type': args.type,
			'ttl': args.ttl
		})