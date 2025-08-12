from pytorch_fid import fid_score

real_path = 'path/to/real_images'
generated_path = 'path/to/generated_images'

fid_value = fid_score.calculate_fid_given_paths([real_path, generated_path],
                                                batch_size=50,
                                                device='cuda',  # 或 'cpu'
                                                dims=2048)
print(f'FID: {fid_value}')