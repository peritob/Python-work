from Bio import SeqIO
with open ("reduced_list_testGH18.txt") as f:
	required_ids = f.read().splitlines()
	
with open("out.fasta","w") as output_handle:
	with open("testGH18.fasta", "rU") as handle:
		for record in SeqIO.parse(handle, "fasta"):
			if record.id in required_ids:
				SeqIO.write(record, output_handle,"fasta")
		
			
		
