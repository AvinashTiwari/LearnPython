class ArticlesController < ApplicationController
  def index
    articles = Article.recent.
      page(current_page).
      per(per_page)
    render json: articles
   end

   def show
   end
end
