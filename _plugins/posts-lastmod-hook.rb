# frozen_string_literal: true

# Set the last modified date of each post from its Git history.
Jekyll::Hooks.register :posts, :post_init do |post|
  commit_num = `git rev-list --count HEAD "#{post.path}"`.to_i
  if commit_num > 1
    lastmod_date = `git log -1 --pretty="%ad" --date=iso "#{post.path}"`.strip
    post.data["last_modified_at"] = lastmod_date
  end
end
